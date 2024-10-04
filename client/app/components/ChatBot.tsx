"use client"

import { useState } from 'react';
import ChatInput from './ChatInput';
import Message from './Message';

type Message = {
  id: number;
  text: string;
  sender: 'user' | 'bot';
  isHtml?: boolean;
};

const ChatBox = () => {
  const [messages, setMessages] = useState<Message[]>([{ id: 0, text: "Hello! How can I assist you today?", sender: "bot" },]);

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
      isHtml: true,    };

    setMessages((prev) => [...prev, botMessage]);
  };

  return (
    <div className="flex flex-col h-screen chat-container ">
      <header className="p-4 text-center font-bold">
        <h1>Chatbot</h1>
      </header>

      <div className="flex-1 border-t p-4">
        {messages.map((msg) => (
          <Message key={msg.id} message={msg} />
        ))}
      </div>

      <ChatInput onSend={sendMessage} />
    </div>
  );
};

export default ChatBox;