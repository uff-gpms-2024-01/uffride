import { defineStore } from 'pinia'

export const useRideRequestStore = defineStore('ride-request', {
  state() {
    return {
			where: '',
      toWhere: '',
      date: '0',
      nowRice: false,
      passengersNumber: 0
    };
  },

  getters: {
    getData() {
      return this.date;
    }
  }

})
