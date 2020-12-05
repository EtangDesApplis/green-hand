import React from 'react'
/*
 * Table definition
 * Table formating
 * table line removal setup
 */

const TableHeader = () => {
    return (
        <thead>
            <tr>
                <th>Variety</th>
                <th>Seeding Outdoor</th>
                <th>Seeding Indoor</th>
                <th>Harvest</th>
                <th>Exposition</th>
                <th>Time to Harvest</th>
                <th>Remove</th>
            </tr>
        </thead>
    )
}

const Table = (props) => {
    const { characterData, removeCharacter } = props

    return (
        <table>
            <TableHeader />
            <TableBody characterData={characterData} removeCharacter={removeCharacter} />
        </table>       
    )
}

const TableBody = (props) => {

    const rows = props.characterData.map((row, index) => {
        return (
            <tr key={index}>
                <td>{row.variety}</td>
                <td>{(() => {
                    var val = ''
                    if (row.seedingOutdoor[0] !== '') {
                        val = JSON.stringify(row.seedingOutdoor.map((month) => (month.label)))
                    }
                    return val
                })()}</td>
                <td>{(() => {
                    var val = ''
                    if (row.seedingIndoor[0] !== '') {
                        val = JSON.stringify(row.seedingIndoor.map((month) => (month.label)))
                    }
                    return val
                })()}</td>
                <td>{(() => {
                    var val = ''
                    if (row.harvest[0] !== '') {
                        val = JSON.stringify(row.harvest.map((month) => (month.label)))
                    }
                    return val
                })()}</td>
                <td>{row.exposition}</td>
                <td>{row.timeToHarvest}</td>
                <td>
                    <button onClick={() => props.removeCharacter(index)}>Delete</button>
                </td>
            </tr>
        )
    })
    return <tbody>{rows}</tbody>
        

}


export default Table