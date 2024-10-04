import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { message } = req.body;

    const apiResponse = await fetch('http://localhost:8000/api/v1/chatbot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    const data = await apiResponse.json();
    res.status(200).json(data);
  } else {
    res.status(405).json({ message: 'Method Not Allowed' });
  }
}
