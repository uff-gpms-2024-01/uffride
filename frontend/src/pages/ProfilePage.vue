<template>
  <q-page class="flex flex-center column">
    <div class="full-width">
      <div class="row justify-center">
        <q-card id="card-profile" class="col-md-8 col-11">
          <q-card-section class="row card-header">
            <div class="col flex column justify-center">
              <div class="text-h6">Pedro</div>
              <div class="text-subtitle2">Reputação</div>
            </div>
            <div class="col flex justify-end">
              <q-avatar size="100px">
                <img src="https://cdn.quasar.dev/img/avatar.png" />
              </q-avatar>
            </div>
          </q-card-section>
          <q-card-section class="card-body">
            <q-form class="row q-gutter-md justify-center content-center">
              <q-input
                rounded
                outlined
                v-model="text"
                label="Email"
                model-value="pedro@gmail.com"
                readonly
                class="col-5"
              />
              <div class="flex-break q-py-md"></div>

              <q-input
                rounded
                outlined
                v-model="text"
                label="CPF"
                model-value="10998148324214"
                readonly
                class="col-5"
              />

              <q-input
                rounded
                outlined
                v-model="text"
                label="Senha"
                model-value=""
                disable
                class="col-5"
              />
            </q-form>
            <q-btn label="Editar" type="submit" color="primary" />
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
defineOptions({
  name: "IndexPage",
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
