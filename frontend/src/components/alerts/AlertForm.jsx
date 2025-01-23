import React, { useState } from 'react';

const AlertForm = () => {
  const [threshold, setThreshold] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log(`Threshold: ${threshold}, Message: ${message}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="threshold">Threshold:</label>
        <input
          type="number"
          id="threshold"
          value={threshold}
          onChange={(e) => setThreshold(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="message">Message:</label>
        <input
          type="text"
          id="message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
      </div>
      <button type="submit">Set Alert</button>
    </form>
  );
};

export default AlertForm;
