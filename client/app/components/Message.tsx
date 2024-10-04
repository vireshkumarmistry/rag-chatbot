import { marked } from "marked";

interface MessageProps {
  message: {
    id: number;
    text: string;
    sender: 'user' | 'bot';
    isHtml?: boolean;
  };
}

const Message = ({ message }: MessageProps) => {
  const formattedText = marked(message.text);

  return (
    <div className={`p-2 ${message.sender === 'user' ? 'text-right' : 'text-left'}`}>
      <div
        className={`inline-block px-4 py-2 rounded ${
          message.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'
        }`}
      >
        {message.isHtml ? (
          <div dangerouslySetInnerHTML={{ __html: formattedText }} />
        ) : (
          message.text
        )}
      </div>
    </div>
  );
};

export default Message;