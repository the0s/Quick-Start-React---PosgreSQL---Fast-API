import TableBody from "./TableBody";
import TableHead from "./TableHead";
import { useSortableTable } from "../functions/useSortableTable";
import { useEffect,  useState } from "react"

const Table = ({caption, data, columns }) => {
const [tableData, setTableData, handleSorting] = useSortableTable(data);
const [change, setChange] = useState(0);


const increament = () =>{
    setChange(change+1)
}

useEffect(() => {
    setTableData(data);
    increament();
    // eslint-disable-next-line react-hooks/exhaustive-deps
}, [data])


 return (
  <>
   <table className="table">
    <caption>{caption}</caption>
    <TableHead {...{ columns, handleSorting, change }} />
    <TableBody {...{ columns, tableData }} />
   </table>
  </>
 );
};

export default Table;