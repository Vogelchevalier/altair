scene = new THREE.Scene();

const container = document.getElementById("my-canvas");
const w = 640;
const h = 480;

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(640, 480);
container.appendChild(renderer.domElement);

camera = new THREE.PerspectiveCamera(70, w / h, 1, 1000);

const geometry = new THREE.BoxGeometry(1, 1, 1, 5, 5, 5);
const material = new THREE.MeshBasicMaterial({ color: 0x212A2F, wireframe: true });
const cube = new THREE.Mesh(geometry, material);

scene.add(cube);

camera.position.z = 3;

function update() {
    cube.rotation.z += 0.005;
    cube.rotation.y += 0.01;
}

function render() {
    renderer.render( scene, camera );
}

function gameLoop() {
    requestAnimationFrame(gameLoop);
    update();
    render();
}

gameLoop();