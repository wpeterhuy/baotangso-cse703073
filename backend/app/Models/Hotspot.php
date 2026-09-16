<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Hotspot extends Model
{
    protected $table = 'hotspots';
    const UPDATED_AT = null;
    protected $fillable = ['scene_id','type','yaw','pitch','label','icon','target_scene_id','artifact_id','audio_url','content_vi','content_en','order_index'];
    public function scene() { return $this->belongsTo(Scene::class); }
    public function targetScene() { return $this->belongsTo(Scene::class, 'target_scene_id'); }
    public function artifact() { return $this->belongsTo(Artifact::class); }
}
