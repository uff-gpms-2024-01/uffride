import { defineStore } from 'pinia'
import { is } from 'quasar';

export const useUserStore = defineStore('user', {
  state() {
    return {
		name: '',
        email: '',
        id: '',
    };
  },

  getters: {
    getUser() {
      return {
        name: this.name,
        email: this.email,
        id: this.id
      };
    },
    isLogged() {
      return is.defined(this.name);
    }
  },

  actions: {
    setUser(user) {
      this.name = user.name;
      this.email = user.email;
      this.id = user.id;
    }
  }
  

  

})
