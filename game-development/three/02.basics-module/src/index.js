import * as THREE from 'three';

// Basic elements of the scene
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75, // Field of view (degrees)
  window.innerWidth / window.innerHeight, //aspect ratio
  0.1, // near clipping plane
  1000 // far clipping plane
);
const renderer = new THREE.WebGLRenderer();

// Scene config
const geometry = new THREE.BoxGeometry(); // Contains the points (vertices) and fill (faces)
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Material with the color
const cube = new THREE.Mesh(geometry, material); // Merges the geometry with the material
scene.add(cube);

// Camera config
camera.position.z = 5;

// Renderer config
renderer.setSize(window.innerWidth, window.innerHeight); // Size of the render
document.body.appendChild(renderer.domElement); // Where to place the render

// Animation config
const animate = () => {
  requestAnimationFrame(animate); // Draw the scene every time the screen is refreshed (usually 60 times per second)
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
};
// Animate!
animate();
