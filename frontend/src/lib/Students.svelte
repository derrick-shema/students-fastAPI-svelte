<script lang="ts">
    import {onMount} from 'svelte';
    type Student = { id: number; first_name: string; last_name: string };
    let students: Student[] = [];

    onMount(async () => {
        const res = await fetch('http://localhost:8000');
        students = await res.json();
    })
</script>

    <div class="bg-white flex flex-col items-center">
        <h2 class="text-3xl font-bold mb-6 text-gray-800">Students</h2>
        <ul class="list-none">
            {#each students as student }
                <li class="bg-orange-500 text-white px-2.5 py-2 mb-2 rounded-lg">
                    <span class="font-semibold">{student.first_name} {student.last_name}</span>
                </li>
            {/each}
        </ul>
    </div>

    
