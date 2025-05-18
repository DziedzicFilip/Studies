@extends('main')
@section ('menu')
<a href="/internal-events/create" class="btn btn-primary" style="text-decoration:none"> create</a>
<a href="/internal-events" class="btn btn-primary" style="text-decoration:none"> all</a>
@endsection
@section ('content')
  <div class="container">
<div class="row gy-3">
<div class="col-sm-12 col-md-6 col-lg-4">
<a href="/internal-events" style="text-decoration:none">
<div class="card">
<div class="card-body">
<p class="card-title h5 text-black clearfix">Internal events</p>
</div>
</div>
</a>
</div>
</div>
</div>
@endsection