import { useState, useEffect } from 'react'
import axios from 'axios'

const useResources = (resource) => {

    // States
    const [resources, setResources] = useState([])

    // Fetch data
    const fetchResource = async (resource) => {
        const res = await axios.get(`https://jsonplaceholder.typicode.com/${resource}`)
        setResources(res.data)
    }

    // useEffect(fn,arr) is run every time the component is rendered
    useEffect(() => {
        fetchResource(resource)
    }, [resource])    // useEffect is only called if the array has changed!

    return resources

}

export default useResources