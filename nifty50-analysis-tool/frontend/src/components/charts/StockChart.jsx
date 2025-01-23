import React, { useRef, useEffect } from 'react';
import * as d3 from 'd3';

const StockChart = ({ data }) => {
  const chartRef = useRef();

  useEffect(() => {
    if (!data || data.length === 0) return;

    const svg = d3.select(chartRef.current);
    const margin = { top: 20, right: 20, bottom: 30, left: 50 };
    const width = +svg.attr('width') - margin.left - margin.right;
    const height = +svg.attr('height') - margin.top - margin.bottom;

    const x = d3.scaleTime().range([0, width]);
    const y = d3.scaleLinear().range([height, 0]);

    const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

    const parseTime = d3.timeParse('%Y-%m-%d');
    data.forEach(d => {
      d.date = parseTime(d.date);
      d.close = +d.close;
      d.open = +d.open;
      d.high = +d.high;
      d.low = +d.low;
    });

    x.domain(d3.extent(data, d => d.date));
    y.domain([d3.min(data, d => d.low), d3.max(data, d => d.high)]);

    g.append('g')
      .attr('class', 'axis axis--x')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x));

    g.append('g')
      .attr('class', 'axis axis--y')
      .call(d3.axisLeft(y));

    const candlestick = g.selectAll('.candlestick')
      .data(data)
      .enter().append('g')
      .attr('class', 'candlestick')
      .attr('transform', d => `translate(${x(d.date)},0)`);

    candlestick.append('line')
      .attr('class', 'stem')
      .attr('y1', d => y(d.high))
      .attr('y2', d => y(d.low))
      .attr('stroke', d => d.close > d.open ? 'green' : 'red');

    candlestick.append('rect')
      .attr('class', 'body')
      .attr('y', d => y(Math.max(d.open, d.close)))
      .attr('height', d => Math.abs(y(d.open) - y(d.close)))
      .attr('width', 5)
      .attr('fill', d => d.close > d.open ? 'green' : 'red');
  }, [data]);

  return (
    <svg ref={chartRef} width="960" height="500"></svg>
  );
};

export default StockChart;
