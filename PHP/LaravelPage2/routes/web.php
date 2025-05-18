<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\InternalEventsController;

Route::get('/', [HomeController::class,"index"]);
Route::get("/internal-events", [InternalEventsController::class,"index"]);
Route::get("/internal-events/edit/{id}", [InternalEventsController::class,"edit"]);
Route::post("/internal-events/update/{id}", [InternalEventsController::class,"update"]);
Route::get("/internal-events/create", [InternalEventsController::class,"create"]);
Route::post("/internal-events/add-to-db", [InternalEventsController::class,"addToDB"]);
Route::get('/internal-events/delete/{id}', [InternalEventsController::class, 'showDelete']);
Route::post('/internal-events/delete/{id}', [InternalEventsController::class, 'delete']);
