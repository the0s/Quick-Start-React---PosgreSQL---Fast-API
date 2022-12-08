import { useState } from "react";
import Table from "./Table";
import { useEffect } from "react"

const BASE_URL = process.env.REACT_APP_API_URL;

const TableFetch = ({year}) => {
    const columns = [
      { label: "Country", accessor: "country", sortable: true },
      { label: "Gold", accessor: "gold", sortable: true },
      { label: "Silver", accessor: "silver", sortable: true },
      { label: "Bronze", accessor: "bronze", sortable: true },
      ];

   const [tableData, setTableData] = useState([]);

   useEffect(() => {
    const y = (year !== 'all') ? year : "";
    const url = BASE_URL + y;
    const fetchData = () => {
        try{
            fetch(url)
            .then((res) => res.json())
            .then((json) => {
                setTableData(json);
            })
        } catch (error) {
            console.log("error", error);
        }
    };
    fetchData();

    }, [year])

   const caption = "Country and medals in year " + year;
   return (     
     <div>
      <Table
          caption={caption}
          data={tableData}
          columns={columns}
      />
      </div>
      );
};

export default TableFetch;