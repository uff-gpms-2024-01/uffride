import { ref } from 'vue';
import axios from 'axios';

export function useRide() {
  const count = ref(0);

	/**
	 *
	 * @param {int} id
	 * @returns
	 */
  const isDriver = (rideId, userID) => {
		// @todo Fazer requisição para verificar se nessa carona o usuário é o motorista
    console.log('oi' +rideId);
		return true;
  }

  function decrement() {
    count.value--;
  }

  return { count, isDriver, decrement };
}
