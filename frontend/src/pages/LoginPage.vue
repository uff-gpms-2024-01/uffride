<template>
	<q-page class="flex flex-center column">
		<h1 class="text-h4">Faça o login</h1>
		<q-form
			@submit.prevent="onSubmit"
			class="q-gutter-lg col-6"
		>
			<q-input
				type="text"
				rounded
				outlined
				label="Email:"
				lazy-rules
				v-model="userName"
				:rules="[(val) => !!val || 'Campo não pode está vazio']"
			/>

			<q-input
				rounded
				outlined
				:type="isPwd ? 'password' : 'text'"
				label="Senha:"
				v-model="password"
				lazy-rules
				:rules="[(val) => !!val || 'Campo não pode está vazio']"
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
							label="Entrar"
							type="submit"
							color="primary"
							class="full-width"
						/>
				</div>
			</div>
		</q-form>

		<span class="q-mt-md"
			>Ou
			<RouterLink to="/cadastro"
				>cadastra-se</RouterLink
			></span
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
import { useRouter } from 'vue-router';
import axios from 'axios';
import BASE_URL_API from 'src/constants/baseUrl';

const isPwd = ref(true);
const userName = ref('');
const password = ref('');
 
const router = useRouter();

 const onSubmit = () => {
	  requestLogin();
};


const requestLogin = async () => {
		const loginForm = {
			email: userName.value,
			password: password.value,
		};
		
		axios.post(BASE_URL_API + '/api/user/login', loginForm).then((response) => {
			if (response.status !== 200) {
				alert(response.text);
				return;
			}
			console.log(response)
			window.localStorage.setItem('user', JSON.stringify(response.data));
			router.push('/');
		}).catch((error) => {
			console.log(error);
			alert(`Erro ao fazer login: ${error.response.data.message}`);
		});
};
</script>
