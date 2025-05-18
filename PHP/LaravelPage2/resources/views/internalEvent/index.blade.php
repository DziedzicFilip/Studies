@extends("main", ['title' => 'Wydarzenia '])
@section ('menu')
<a href="/internal-events/create" class="btn btn-primary" style="text-decoration:none"> create</a>
<a href="/internal-events" class="btn btn-primary" style="text-decoration:none"> all</a>
@endsection
@section("content")
<div class="container">
<div class="row gy-3">
    @foreach($models as $model)
    <div class="card">
        <div class="card-body">
            <p class="card-title h5">{{$model->Title}}</p>
            <p><strong>{{$model->ShortDescription}}</strong></p>
            {!! $model->ContentHTML !!}
        </div>
        <div class="card-footer">
            <a href="{{url()->current()}}/edit/{{$model->Id}}">Edit</a>
            <a href="{{url()->current()}}/delete/{{$model->Id}}">Delete</a>
        </div>
    </div>
    @endforeach
</div>
</div>
@endsection