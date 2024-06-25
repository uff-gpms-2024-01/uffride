<template>
	<q-page class="flex flex-center column">
		<div class="full-width">
			<div class="row justify-center">
				<q-card id="card-profile" class="col-md-8 col-11">
					<q-card-section class="row card-header">
						<div class="col flex column justify-center">
							<div class="text-h6">
								{{ user.name }}
							</div>
							<q-rating
								size="18px"
								:model-value="3"
								:max="5"
								readonly
							/>
						</div>
						<div class="col flex justify-end">
							<q-avatar size="100px">
								<img
									src="https://www.kindpng.com/picc/m/52-526237_avatar-profile-hd-png-download.png"
								/>
							</q-avatar>
						</div>
					</q-card-section>
					<q-card-section class="card-body">
						<q-form
							ref="form"
							@submit="saveProfile"
							class="row q-gutter-md justify-center content-center"
						>
							<q-input
								rounded
								outlined
								v-model="user.email"
								label="Email"
								readonly
								class="col-12 col-md-5"
							/>

							<q-input
								v-if="edit"
								rounded
								outlined
								v-model="name"
								label="Nome"
								class="col-12 col-md-5"
							/>

							<q-input
								rounded
								outlined
								v-model="password"
								label="Senha"
								:disable="!edit"
								class="col-12 col-md-5"
								type="password"
								:rules="[
									(val) =>
										val == passwordConfirm ||
										'Senhas diferentes'
								]"
								lazy-rules
							/>

							<q-input
								v-if="edit"
								rounded
								outlined
								label="Confirmar senha"
								v-model="passwordConfirm"
								:disable="!edit"
								class="col-12 col-md-5"
								type="password"
							/>
						</q-form>
					</q-card-section>
					<q-card-actions>
						<q-btn
							:label="!edit ? 'Editar' : 'Cancelar edição'"
							:color="edit ? 'red' : 'primary'"
							@click="edit = !edit"
						/>

						<q-btn
							v-if="edit"
							label="Salvar"
							type="submit"
							color="primary"
							@click="form.submit()"
						/>
					</q-card-actions>
				</q-card>
			</div>
		</div>
	</q-page>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';
import BASE_URL_API from 'src/constants/baseUrl';
import axios from 'axios';

const user = ref({});
const edit = ref(false);
const name = ref('');
const password = ref('');
const passwordConfirm = ref('');
const form = ref('');

onBeforeMount(() => {
	getProfile().then((result) => {
		user.value = result;
		name.value = user.value.name;
	});
});

// @todo pegar o id do usuario em algum canto
const getProfile = async (id = 1) => {
	const response = await axios.get(
		`${BASE_URL_API}/api/user/${id}`
	);
	// console.log(response.data);
	return response.data;
};

const saveProfile = () => {
	const body = {
		name: name.value,
		password: password.value
	};
	axios
		.put(`${BASE_URL_API}/api/user/${user.value.id}`, body)
		.then((response) => {
			user.value = getProfile();
			edit.value = false;
		})
		.catch((error) => {
			console.error(error);
		});
};
</script>

<style>
/* #card-profile {
  height: 50vh;
} */
.card-header {
	background-color: rgb(7, 106, 255);
	color: aliceblue;
}
.card-body {
	height: 30vh;
}
</style>
