<script>
    import {onMount} from 'svelte';
    let students=[];

    onMount(async () => {
        const res = await fetch('http://localhost:8000');
        students = await res.json();
    })
</script>