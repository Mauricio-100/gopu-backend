import express from 'express';
import dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';

dotenv.config();
const app = express();
app.use(express.json());

// Initialisation Gemini
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: 'gemini-pro' });

// Middleware de vérification du token
function verifyToken(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Token manquant ou invalide' });
  }

  const token = auth.split(' ')[1];
  if (token !== process.env.AGENT_TOKEN) {
    return res.status(403).json({ error: 'Accès refusé' });
  }

  next();
}

// Endpoint sécurisé
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

// Endpoint public
app.get('/', (req, res) => {
  res.send('✅ GopuOS Agentic Backend is running');
});

// Endpoint de statut
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

// Lancement du serveur
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => {
  console.log(`🚀 Backend GopuOS actif sur le port ${PORT}`);
});
