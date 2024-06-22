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
				label="Usuário:"
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
					<RouterLink to="/">
						<q-btn
							rounded
							label="Entrar"
							type="submit"
							color="primary"
							class="full-width"
						/>
					</RouterLink>
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

const isPwd = ref(true);
const userName = ref('');
const password = ref('');
/**
 * Login
 */
 const onSubmit = () => {
	// @TODO Criar chamada api para login
	console.log("oi");
};
</script>
