import express from 'express';
import dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';

dotenv.config();
const app = express();
app.use(express.json());

// Initialisation Gemini
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: 'gemini-pro' });

// Middleware Bearer simple
function verifyToken(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Token manquant ou invalide' });
  }

  const token = auth.slice(7);
  if (token !== process.env.AGENT_TOKEN) {
    return res.status(403).json({ error: 'Accès refusé' });
  }

  next();
}

// 🔐 Endpoint sécurisé
app.post('/agent', verifyToken, async (req, res) => {
  const { prompt } = req.body;
  try {
    const result = await model.generateContent(prompt);
    const output = result.response.text();
    res.json({ output });
  } catch (err) {
    console.error('❌ Erreur Gemini:', err.message);
    res.status(500).json({ error: 'Erreur agentique' });
  }
});

// 🧠 Endpoint token-info
app.get('/token-info', verifyToken, (req, res) => {
  res.json({
    verified: true,
    token: 'sk-***************',
    role: 'admin',
    agent: 'Gemini',
    issued_by: 'GopuOS',
    expires: 'never'
  });
});

// 🏷️ Badge “Verified”
app.get('/badge', (req, res) => {
  res.redirect('https://img.shields.io/badge/GopuOS-Verified-blue?logo=linux');
});

// 📊 Statut système
app.get('/status', (req, res) => {
  res.json({
    status: '🟢 Online',
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    agent: 'Gemini',
    kernel: 'Agentic LLM',
    version: '1.0.0'
  });
});

// 🏁 Accueil
app.get('/', (req, res) => {
  res.send('✅ GopuOS Agentic Backend is running');
});

// pour savoir si il fonction
app.get('/test-gemini', async (req, res) => {
  try {
    const result = await model.generateContent('ping');
    res.send(result.response.text());
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});


// 🚀 Lancement
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => {
  console.log(`🚀 Backend GopuOS actif sur le port ${PORT}`);
});
