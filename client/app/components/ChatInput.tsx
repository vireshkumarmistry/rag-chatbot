"use client"

import { useState } from 'react';

interface ChatInputProps {
  onSend: (message: string) => void;
}

const ChatInput = ({ onSend }: ChatInputProps) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      onSend(input);
      setInput('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex p-4 bg-gray-100">
      <input
        type="text"
        className="flex-1 p-2 border rounded"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button type="submit" className="ml-2 px-4 py-2 bg-blue-500 text-white rounded">
        Send
      </button>
    </form>
  );
};

export default ChatInput;
