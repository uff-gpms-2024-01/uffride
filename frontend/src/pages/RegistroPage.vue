<template>
	<q-page class="flex flex-center column">
		<h1 class="text-h4">Cadastro</h1>
		<span class="text-subtitle1 text-grey-9 q-ma-sm"
			>Digite seus dados abaixo para realizar o
			cadastro</span
		>
		<q-form
			@submit.prevent="onSubmit"
			class="q-gutter-lg col-6"
		>
			<q-input
				type="text"
				rounded
				outlined
				label="Digiter seu email:"
				lazy-rules
				v-model="userEmail"
				:rules="[
					(val) => !!val || 'Esse campo é obrigatório',
				]"
			/>

			<q-input
				type="text"
				rounded
				outlined
				label="Digite seu nome:"
				lazy-rules
				v-model="userName"
				:rules="[
					(val) => !!val || 'Esse campo é obrigatório',
				]"
			/>

			<q-input
				rounded
				outlined
				:type="isPwd ? 'password' : 'text'"
				label="Senha:"
				v-model="password"
				lazy-rules
				:error="confirmPassword != password"
				:rules="[(val) => !!val || 'Senha é necessária']"
			>
				<template v-slot:append>
					<q-icon
						:name="isPwd ? 'visibility_off' : 'visibility'"
						class="cursor-pointer"
						@click="isPwd = !isPwd"
					/>
				</template>
			</q-input>

			<q-input
				rounded
				outlined
				:type="isPwd ? 'password' : 'text'"
				label="Confirmar senha:"
				v-model="confirmPassword"
				lazy-rules
				:error="confirmPassword != password"
				:rules="[(val) => !!val || 'Senha é necessária']"
			>
				<template v-slot:append>
					<q-icon
						:name="isPwd ? 'visibility_off' : 'visibility'"
						class="cursor-pointer"
						@click="isPwd = !isPwd"
					/>
				</template>
			</q-input>

			<div class="row justify-center">
				<div class="col-5">
					<q-btn
						rounded
						label="Cadastrar"
						type="submit"
						color="primary"
						class="full-width"
					/>
				</div>
			</div>
		</q-form>

		<span class="q-mt-md"
			>Já possui conta?
			<RouterLink to="/login">Entrar</RouterLink></span
		>
	</q-page>
</template>

<style scoped>
.w-form {
	width: 30%;
}
</style>

<script setup >
import { ref } from 'vue';
import axios from 'axios';
import BASE_URL_API from 'src/constants/baseUrl';
import { useRouter } from 'vue-router';

const isPwd = ref(true);
const userName = ref('');
const userEmail = ref('');
const password = ref('');
const confirmPassword = ref('');

const router = useRouter();

/**
 * Criação de usuário
 */
const onSubmit = () => {
	
	createUser();
};
const createUser = async () => {
		const createUserForm = {
			email: userEmail.value,
			password: password.value,
			name: userName.value,
		};
		
		axios.post(BASE_URL_API + '/api/user/register', createUserForm).then((response) => {
			if (response.status !== 201) {
				alert(response.text);
				return;
			}
			window.localStorage.setItem('user', JSON.stringify(response.data));
			window.localStorage.setItem('user_id', response.data.id);
			router.push('/');
		}).catch((error) => {
			console.log(error);
			alert(`Erro ao cadastrar: ${error.response.data.message}`);
		});
};
</script>
