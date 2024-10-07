"use client"

import { useEffect, useState } from 'react';
import EmojiPicker from 'emoji-picker-react';
import { FiPaperclip, FiSmile } from 'react-icons/fi'

interface ChatInputProps {
    onSend: (message: string) => void;
}

const ChatInput = ({ onSend }: ChatInputProps) => {
    const [input, setInput] = useState<string>('');
    const [showEmojiPicker, setShowEmojiPicker] = useState<boolean>(false);


    const handleEmojiClick = (emojiObject: { emoji: string }) => {
        setInput((prevInput) => prevInput + emojiObject.emoji);
    };

    const handleOutsideClick = (e: any) => {
        if (!e.target.closest(".emoji-picker-react") && !e.target.closest(".emoji-toggle")) {
            setShowEmojiPicker(false);
        }
    };

    useEffect(() => {
        if (showEmojiPicker) {
            document.addEventListener("click", handleOutsideClick);
        } else {
            document.removeEventListener("click", handleOutsideClick);
        }
        return () => {
            document.removeEventListener("click", handleOutsideClick);
        };
    }, [showEmojiPicker]);

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
        <form onSubmit={handleSubmit}>
            <div className="flex items-center justify-between p-3 border-t border-gray-300 gap-x-4">
                <div className="relative">
                    <div
                        onClick={() => setShowEmojiPicker(!showEmojiPicker)}
                        className="text-gray-600 hover:text-gray-800 cursor-pointer"
                    >
                        <FiSmile size={24} />
                    </div>

                    {showEmojiPicker && (
                        <div className="absolute bottom-12 left-0 z-10 emoji-picker-react">
                            <EmojiPicker onEmojiClick={handleEmojiClick} />
                        </div>
                    )}
                </div>

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
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
                    </svg>

                </button>
            </div>
        </form>
    );
};

export default ChatInput;