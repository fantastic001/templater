import { API_URL } from "./../../config";
import axios from "axios"

export default class {{ name }}Service 
{
    constructor(self) 
    {
        this.self = self;
    }

    static list() 
    {
        return axios.get(API_URL + "/{{ endpoint}}/");
    }

    static get(id) 
    {
        return axios.get(API_URL + "/{{ endpoint }}/" + id);
    }
    
    {% for service in item_endpoints %}
    {% if service["type"].lower() == "get"%}
    static {{ service["name"]}}(id) 
    {
        return axios.get(API_URL + "/{{ endpoint }}/" + id + "/{{ service["name"]}}");
    }
    {% else %}
    static {{service["name"]}}(id, data) 
    {
        return axios.post(API_URL + "/{{ endpoint }}/" + id + "/{{service["name"]}}");
    }
    {% endif %}
    {% endfor %}

    static create(x)
    {
        return axios.post(API_URL + "/{{ endpoint }}/", x);
    }

    static update(id, data) 
    {
        return axios.post(API_URL + "/{{ endpoint }}/" + id, data);
    }

    static delete(id) 
    {
        return axios.delete(API_URL + "/{{endpoint}}/" + id);
    }
}
