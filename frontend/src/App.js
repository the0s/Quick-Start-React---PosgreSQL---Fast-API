import React from "react";
import './App.css';
import TableFetch from "./components/TableFetch";
import Select from 'react-select'
import { useState } from "react";


function App() {
  const options = [
    { value: 2004, label: '2004' },
    { value: 2008, label: '2008' },
    { value: 2012, label: '2012' },
    { value: "all", label: 'All' },
    ]   
  
  const [year, setYear] = useState(2012);
  
  return (
    <div className = "App">     
    
      <div className="select">
        <Select options={options} 
        defaultValue={{ value: 2012, label: '2012' }}
        onChange={(choice) => setYear(choice.value)}
        />
      </div>

      <div className="table_container">
       <TableFetch year={year}/>
      </div>  

    </div> 
    );
}

export default App;