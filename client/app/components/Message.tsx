interface MessageProps {
    message: {
      id: number;
      text: string;
      sender: 'user' | 'bot';
    };
  }
  
  const Message = ({ message }: MessageProps) => {
    return (
      <div className={`p-2 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
        <div className={`inline-block px-4 py-2 rounded ${message.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}>
          {message.text}
        </div>
      </div>
    );
  };
  
  export default Message;
  