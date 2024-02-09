import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import axios from 'axios';

import './App.css';

function App() {
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [result, setResult] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    try {
      if (endDate < startDate) {
        setError('End date cannot be earlier than start date');
        return;
      }

      const response = await axios.get(
        `/api/top_hashtags?start_date=${startDate.toISOString()}&end_date=${endDate.toISOString()}`
      );
      setResult(response.data.top_hashtags);
      setError('');
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="app-container">
      <h1>Hashtag Analyzer</h1>
      <div className="date-picker-container">
        <label>Start Date:</label>
        <DatePicker
          selected={startDate}
          onChange={(date) => setStartDate(date)}
        />
      </div>
      <div className="date-picker-container">
        <label>End Date:</label>
        <DatePicker
          selected={endDate}
          onChange={(date) => setEndDate(date)}
          minDate={startDate}
        />
      </div>
      <button className="submit-button" onClick={handleSubmit}>
        Submit
      </button>
      {error && <div className="error-message">{error}</div>}
      <div className="result-container">
        <h2>Result:</h2>
        <table>
          <thead>
            <tr>
              <th>Hashtag</th>
              <th>Clicks</th>
            </tr>
          </thead>
          <tbody>
            {result.map(({ 0: hashtag, 1: clicks }) => (
              <tr key={hashtag}>
                <td>{hashtag}</td>
                <td>{clicks}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
