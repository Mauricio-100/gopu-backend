import express from 'express';
import dotenv from 'dotenv';
import { GoogleGenerativeAI } from '@google/generative-ai';

dotenv.config();
const app = express();
app.use(express.json());

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: 'gemini-pro' });

app.post('/agent', async (req, res) => {
  const { prompt } = req.body;
  try {
    const result = await model.generateContent(prompt);
    const response = result.response.text();
    res.json({ output: response });
  } catch (err) {
    console.error('❌ Erreur Gemini:', err.message);
    res.status(500).json({ error: 'Erreur agentique' });
  }
});

app.get('/', (req, res) => {
  res.send('✅ GopuOS Agentic Backend is running');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 GopuOS backend actif sur le port ${PORT}`);
});
