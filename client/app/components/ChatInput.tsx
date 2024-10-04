"use client"

import { useState } from 'react';
import  EmojiPicker  from 'emoji-picker-react';
import { FiPaperclip, FiSmile } from 'react-icons/fi'

interface ChatInputProps {
    onSend: (message: string) => void;
}

const ChatInput = ({ onSend }: ChatInputProps) => {
    const [input, setInput] = useState('');
    const [showEmojiPicker, setShowEmojiPicker] = useState(false);

    const handleEmojiClick = (emojiObject: any) => {
        setInput(input + emojiObject.emoji);
    };

    const handleFileUpload = (event: any) => {
        const file = event.target.files[0];
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (input.trim()) {
            onSend(input);
            setInput('');
        }
    };

    return (
        <div className="flex items-center justify-between p-3 border-t border-gray-300 gap-x-4">
            <button
                onClick={() => setShowEmojiPicker(!showEmojiPicker)}
                className="text-gray-600 hover:text-gray-800"
            >
                <FiSmile size={24} />
            </button>

            {showEmojiPicker && (
                <div className="absolute bottom-12 left-0 z-10">
                    <EmojiPicker onEmojiClick={handleEmojiClick} />
                </div>
            )}

            <input
                type="text"
                className="flex-grow p-2 border rounded-lg"
                placeholder="Type your message..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />

            <input
                type="file"
                id="file-input"
                className="hidden"
                onChange={handleFileUpload}
            />
            <label htmlFor="file-input">
                <FiPaperclip size={24} className="text-gray-600 hover:text-gray-800" />
            </label>

            <button
                onClick={handleSubmit}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
            >
                Send
            </button>
        </div>
    );
};

export default ChatInput;