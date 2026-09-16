<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class VisitEvent extends Model
{
    protected $table = 'visit_events';
    const UPDATED_AT = null;
    protected $fillable = ['session_id','scene_id','hotspot_id','event_type'];
    public function session() { return $this->belongsTo(VisitSession::class); }
    public function scene() { return $this->belongsTo(Scene::class); }
    public function hotspot() { return $this->belongsTo(Hotspot::class); }
}
