import React from 'react';
import StockChart from '../../components/charts/StockChart';
import AlertForm from '../../components/alerts/AlertForm';
import NewsCard from '../../components/news/NewsCard';
import { useStockData } from '../../hooks/useStockData';

const Dashboard = () => {
  const { data: stockData, error: stockError } = useStockData('/api/stock-data');
  const news = [
    { title: 'Market News 1', description: 'Description 1', sentiment: 'positive' },
    { title: 'Market News 2', description: 'Description 2', sentiment: 'negative' },
  ];

  return (
    <div>
      <h1>Dashboard</h1>
      <div>
        <h2>Stock Chart</h2>
        {stockError ? <p>Error loading stock data</p> : <StockChart data={stockData} />}
      </div>
      <div>
        <h2>Set Alerts</h2>
        <AlertForm />
      </div>
      <div>
        <h2>News</h2>
        {news.map((item, index) => (
          <NewsCard key={index} title={item.title} description={item.description} sentiment={item.sentiment} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
