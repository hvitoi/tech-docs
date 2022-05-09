import axios from 'axios'

// Create an instance of axios to request (but do not submit yet)
export default axios.create({
    baseURL: 'https://api.unsplash.com',
    headers: { 
        Authorization: 'Client-ID f78S66joyEAFAoaafCVcChhSX_kYK1UHC2jlqHmFfQ4'
    }
})