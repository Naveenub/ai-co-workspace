import React from "react";

interface MessageBubbleProps {
  message: string;
  fromUser?: boolean;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message, fromUser = false }) => {
  return (
    <div className={`mb-2 p-2 rounded ${fromUser ? "bg-blue-400 text-white ml-auto" : "bg-gray-200"}`}>
      {message}
    </div>
  );
};

export default MessageBubble;
