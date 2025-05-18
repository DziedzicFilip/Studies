<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\InternalEvent;

class InternalEventsController extends Controller
{
    public function index()
    {
        $models = InternalEvent::where("IsActive", "=",true)->get();
           
       return view("internalEvent.index", [
    'models' => $models,
]);
    }
    public function edit($id)
    {
        $model = InternalEvent::find($id);
        return view("internalEvent.edit", [
            'model' => $model,
        ]);
    }
    public function update($id, Request $request){
        $model = InternalEvent::find($id);
        $model->Title = $request->input("Title");
        $model->Link = $request->input("Link");
        $model->ShortDescription = $request->input("ShortDescription");
        $model->ContentHTML = $request->input("ContentHTML");
        $model->MetaTags = $request->input("MetaTags");
        $model->MetaDescription = $request->input("MetaDescription");
        $model->Notes = $request->input("Notes");
        $model->EventDateTime = $request->input("EventDateTime");
        $model->PublishDateTime = $request->input("PublishDateTime");
        $model->IsPublic = $request->input("IsPublic") ? true : false;
        $model->IsCancelled = $request->input("IsCancelled") ? true : false;
        $model->save();
 
        return redirect('/internal-events');
    }
     public function delete($id, Request $request){
        $model = InternalEvent::find($id);
         $model->IsActive = false; 
        $model->save();
        return redirect('/internal-events');
    }
    public function showDelete($id)
{
    $model = InternalEvent::findOrFail($id);
    return view('internalEvent.delete', ['model' => $model]);
}
    public function create()
    {
        $model = new InternalEvent();
        $model->EventDateTime = date("Y-m-d");
        $model->PubishDateTime = date("Y-m-d");
        return view("internalEvent.create",["model"=>$model]);
    }
   public function addToDB(Request $request)
{
    $model = new InternalEvent();
    $model->Title = $request->input("Title");
    $model->Link = $request->input("Link");
    $model->ShortDescription = $request->input("ShortDescription");
    $model->ContentHTML = $request->input("ContentHTML");
    $model->MetaTags = $request->input("MetaTags");
    $model->MetaDescription = $request->input("MetaDescription");
    $model->Notes = $request->input("Notes");
    $model->EventDateTime = $request->input("EventDateTime");
    $model->PublishDateTime = $request->input("PublishDateTime");
    $model->IsPublic = $request->input("IsPublic") ? true : false;
    $model->IsCancelled = $request->input("IsCancelled") ? true : false;
    $model->IsActive = true; 
    $model->CreationDateTime = now();
    $model->EditDateTime = now();
    $model->save();

    return redirect('/internal-events');
}
}
