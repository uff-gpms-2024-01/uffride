<template>
	<q-page class="flex flex-center column">
		<div class="full-width">
			<div class="row justify-center">
				<q-card id="card-profile" class="col-md-8 col-11">
					<q-card-section class="row card-header">
						<div class="col flex column justify-center">
							<div class="text-h6">
								{{ user.user.name }}
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
								<img :src="user.user.photo" />
							</q-avatar>
						</div>
					</q-card-section>
					<q-card-section class="card-body">
						<q-form
							class="row q-gutter-md justify-center content-center"
						>
							<q-input
								rounded
								outlined
								v-model="text"
								label="Email"
								:model-value="user.user.email"
								:readonly="!edit"
								class="col-12 col-md-5"
							/>

							<q-input
								rounded
								outlined
								v-model="text"
								label="Senha"
								model-value="***********"
								:disable="!edit"
								class="col-12 col-md-5"
							/>

							<q-input
								v-if="edit"
								rounded
								outlined
								v-model="text"
								label="Confirmar senha"
								model-value="***********"
								:disable="!edit"
								class="col-12 col-md-5"
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
							@click="saveProfile"
						/>
					</q-card-actions>
				</q-card>
			</div>
		</div>
	</q-page>
</template>

<script setup>
import { onBeforeMount, ref } from 'vue';

const user = ref(null);
const edit = ref(false);

const getProfile = () => {
	// @todo Fazer requisição que retorna os dados de perfil.
	const esperado = `{
		"data": {
			"user": {
				"id": "1",
				"name": "Pedro",
				"email": "pedro@gmail.como",
				"photo": "https://cdn.quasar.dev/img/avatar.png"
			}
		}
	}`;
	return JSON.parse(esperado);
};

const saveProfile = () => {
	// @todo requisição para update do perfil
};

onBeforeMount(() => {
	user.value = getProfile().data;
});
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
