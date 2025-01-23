import React, { useState } from 'react';

const Analysis = () => {
  const [indicator, setIndicator] = useState('');
  const [parameters, setParameters] = useState({});

  const handleIndicatorChange = (e) => {
    setIndicator(e.target.value);
  };

  const handleParameterChange = (e) => {
    const { name, value } = e.target;
    setParameters((prevParams) => ({
      ...prevParams,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log(`Indicator: ${indicator}, Parameters: ${JSON.stringify(parameters)}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="indicator">Indicator:</label>
        <select id="indicator" value={indicator} onChange={handleIndicatorChange}>
          <option value="">Select an indicator</option>
          <option value="rsi">RSI</option>
          <option value="macd">MACD</option>
          <option value="sma">SMA</option>
        </select>
      </div>
      <div>
        <label htmlFor="parameter1">Parameter 1:</label>
        <input
          type="text"
          id="parameter1"
          name="parameter1"
          value={parameters.parameter1 || ''}
          onChange={handleParameterChange}
        />
      </div>
      <div>
        <label htmlFor="parameter2">Parameter 2:</label>
        <input
          type="text"
          id="parameter2"
          name="parameter2"
          value={parameters.parameter2 || ''}
          onChange={handleParameterChange}
        />
      </div>
      <button type="submit">Configure Indicator</button>
    </form>
  );
};

export default Analysis;
