"use client"

import { useState } from 'react';
import ChatInput from './ChatInput';
import Message from './Message';

type Message = {
  id: number;
  text: string;
  sender: 'user' | 'bot';
};

const ChatBox = () => {
  const [messages, setMessages] = useState<Message[]>([]);

  const sendMessage = async (message: string) => {
    const userMessage: Message = {
      id: messages.length + 1,
      text: message,
      sender: 'user',
    };

    setMessages((prev) => [...prev, userMessage]);

    const response = await fetch('http://localhost:8000/api/v1/chatbot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    const botMessage: Message = {
      id: messages.length + 2,
      text: data.message,
      sender: 'bot',
    };

    setMessages((prev) => [...prev, botMessage]);
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 p-4 overflow-y-scroll">
        {messages.map((msg) => (
          <Message key={msg.id} message={msg} />
        ))}
      </div>
      <ChatInput onSend={sendMessage} />
    </div>
  );
};

export default ChatBox;