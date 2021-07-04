import axios from 'axios';
import moment from 'moment';

export const state = () => ({
  camerasList: [],
  alertsList: [],
  lastChecked: 0,
})

export const getters = {
  // Cameras
  getCameras(state) {
    return state.camerasList
  },
  // Alerts
  getAlerts(state) {
    return state.alertsList
  },
  getLastChecked(state) {
    return state.lastChecked
  },
}

export const mutations = {
  // Camers
  setCameras(state, content) {
    state.camerasList = content
  },
  editCameraList(state, content) {
    let index = state.camerasList.findIndex(c => c.id === content.id)
    index>=0 ? state.camerasList[index] = content : state.camerasList.push(content)
  },
  removeCamera(state, id) {
    let filtered = state.camerasList.filter(c => c.id != id)
    state.camerasList = filtered
  },
  // Alerts
  setAlerts(state, content) {
    state.alertsList = content
  },
  setLastChecked(state, content) {
    state.lastChecked = content
  },
}

export const actions = {
  async nuxtServerInit({commit, dispatch}) {
    // Cameras
    const responseCameras = await axios.get(process.env.baseUrl + '/camera/all');
    const allCameras = responseCameras.data;
    commit("setCameras", allCameras);
    // Alerts
    await dispatch('fetchAlerts');
  },
  // Cameras
  async editCamera({commit}, camera) {
    let json = JSON.stringify(camera)
    let headers = {
      'Content-Type': 'application/json'
    }
    const response = camera.id ?
      await axios.post(process.env.baseUrl + '/camera/' + camera.id + '/edit', json, {headers: headers}) :
      await axios.post(process.env.baseUrl + '/camera/create', json, {headers: headers})

    const content = response.data.data;
    commit("editCameraList", content);
  },
  async deleteCamera({commit}, id) {
    const response = await axios.get(process.env.baseUrl + '/camera/' + id + '/delete')
    const resp = response.data.success;
    if (resp) commit("removeCamera", id)
  },
  // Alerts
  async fetchAlerts({commit}) {
    const responseAlerts =  await axios.get(process.env.baseUrl + '/alert/all');
    const allAlerts = responseAlerts.data;
    commit("setAlerts", allAlerts);
    var timestamp = moment().format('x')
    commit("setLastChecked", timestamp);
  },

}
