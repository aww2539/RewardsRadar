import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:5000/api',
    timeout: 1000,
    
  })

const request = instance

export default request
