<template>
    <img :src="GrainImg" alt="Grain image" class="absolute z-10 top-0 left-0 opacity-40 w-screen h-screen">
    <div class=" bg-[#D3ECD0] h-32 animate-pulse duration-[20s] w-32 absolute bottom-12 z-0 rounded-full blur-3xl">
    </div>
    <main class="px-12 text-center  bg-neutral-800 h-screen flex justify-center items-center flex-col">
        <h1 class="text-white text-6xl leading-tight">Welcome to Daylio-AI</h1>
        <p class="text-2xl text-white mt-10 leading-loose">To get started, upload your exported daylio file here</p>
        <div class="card z-20 w-full sm:w-1/2 mt-3">
            <Toast />
            <!-- @vue-ignore -->
            <FileUpload name="daylio-csv-file" url="/api/upload" @upload="onAdvancedUpload($event)" :multiple="false"
                accept="image/*">
                <template #empty>
                    <span>Drag and drop files to here to upload.</span>
                </template>
            </FileUpload>
        </div>
        <div>
            Made with love ♡
        </div>
        <a href="https://github.com/Ara-O/Daylio-AI" target="_blank"> <img :src="GithubLogo" alt="Github logo"
                class="invert w-5 absolute bottom-5 right-5 cursor-pointer"></a>
    </main>
</template>

<script lang="ts" setup>
import GrainImg from "@/assets/grain.png"
import GithubLogo from "@/assets/github-logo.png"
import { useToast } from "primevue/usetoast";
import { FileUpload } from "primevue";

const toast = useToast();

const onAdvancedUpload = () => {
    console.log("eee")
    toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 });
};

</script>

<style></style>