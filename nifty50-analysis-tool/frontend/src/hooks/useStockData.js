import { useState, useEffect } from 'react';

const useStockData = (url) => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const eventSource = new EventSource(url);

    eventSource.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setData((prevData) => [...prevData, ...newData]);
    };

    eventSource.onerror = (err) => {
      setError(err);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [url]);

  return { data, error };
};

export default useStockData;
