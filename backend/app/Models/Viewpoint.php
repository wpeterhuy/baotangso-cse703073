<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Viewpoint extends Model
{
    protected $table = 'viewpoints';
    public $timestamps = false;
    protected $fillable = ['scene_id','yaw','pitch','fov'];
    public function scene() { return $this->belongsTo(Scene::class); }
}
