import React from 'react';

const NewsCard = ({ title, description, sentiment }) => {
  const sentimentColor = sentiment === 'positive' ? 'green' : sentiment === 'negative' ? 'red' : 'gray';

  return (
    <div style={{ border: `2px solid ${sentimentColor}`, padding: '10px', margin: '10px' }}>
      <h2>{title}</h2>
      <p>{description}</p>
      <p style={{ color: sentimentColor }}>{sentiment}</p>
    </div>
  );
};

export default NewsCard;
