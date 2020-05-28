const canvas = document.querySelector('#c');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
const scene = new THREE.Scene();
var clock = new THREE.Clock();

// CAMERA
const fov = 75;
const aspect = 2;
const near = 0.1;
const far = 1000;
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
camera.position.z = 15;

// MAGIC NUMBERS
const earth_rotation_speed = 0.072921159; // 7.2921159 × 10**-5 rad/s TIMES 1000
const earth_tilt = 0.4090465336; // rad

const moon_rotation_speed = 0.03; // Set this to the orbital period
const moon_tilt = 0.0269199584 // rad

// EARTH
const earth_geometry = new THREE.SphereGeometry(5, 32, 32);
const earth_material = new THREE.MeshBasicMaterial({ color: 0x3074AE, wireframe: true });
const earth = new THREE.Mesh(earth_geometry, earth_material);
earth.rotation.z = earth_tilt;
scene.add(earth);

// MOON
const moon_geometry = new THREE.SphereGeometry(2, 16, 16);
const moon_material = new THREE.MeshBasicMaterial({ color: 0xE2E1E7, wireframe: true });
const moon = new THREE.Mesh(moon_geometry, moon_material);
moon.rotation.z = moon_tilt;
moon.position.x = 7;
moon.position.y = 3;
moon.position.z = 5;
//scene.add(moon);

function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
        renderer.setSize(width, height, false);
    }
    return needResize;
}


function physics() {
    var dt = clock.getDelta();
    earth.rotateY(earth_rotation_speed * dt);
    moon.rotateY(moon_rotation_speed * dt);
}

function update() {
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
    }
    physics()
}

function render() {
    renderer.render(scene, camera);
}

function gameLoop() {
    requestAnimationFrame(gameLoop);
    update();
    render();
}

gameLoop();