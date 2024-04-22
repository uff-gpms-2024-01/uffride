<template>
  <q-page class="flex flex-center column">
    <div class="row justify-center full-width map">
      <iframe
        class="col-md-5 col-11"
        src="https://www.openstreetmap.org/export/embed.html?bbox=-43.143889904022224%2C-22.911084460622646%2C-43.115737438201904%2C-22.89465885163995&amp;layer=mapnik"
        style="border: 0px solid black; border-radius: 10px"
      ></iframe>
    </div>

    <q-form @submit="onSubmit" class="q-gutter-md full-width q-mt-sm">
      <div class="row justify-center">
        <q-input
          rounded
          outlined
          v-model="where"
          label="De onde?"
          class="col-md-5 col-8"
          lazy-rules
        />
      </div>

      <div class="row justify-center">
        <q-input
          rounded
          outlined
          type="text"
          v-model="toWhere"
          label="Para onde?"
          lazy-rules
          class="col-md-5 col-8"
        />
      </div>

      <div class="row justify-center">
        <div class="col-3">
          <q-btn
            label="Buscar"
            type="submit"
            color="primary"
            class="full-width"
          />
        </div>
      </div>
    </q-form>
  </q-page>
</template>

<script setup>
defineOptions({
  name: "IndexPage",
});
</script>

<style>
.map {
  height: 40vh;
}
</style>
