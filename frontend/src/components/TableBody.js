const getCountryISO2 = require("../functions/countryISOMapping");

const TableBody = ({ tableData, columns }) => {
 return (
  <tbody>
   {tableData.map((data) => {
    return (
     <tr key={data.country}>
      {columns.map(({ accessor }) => {
       const tData = data[accessor] ? data[accessor] : 0;
       const cl = accessor === "country" 
       ? "fi fi-" + getCountryISO2(data.code).toLowerCase() 
       : "";
       return <td key={accessor}>
       <div className={cl}/> {tData}
       </td>;
      })}
     </tr>
    );
   })}
  </tbody>
 );
};

export default TableBody;