<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class VisitSession extends Model
{
    protected $table = 'visit_sessions';
    const UPDATED_AT = null;
    protected $fillable = ['user_id','guest_token','museum_id','tour_id','mode','started_at','ended_at','duration_sec'];
    protected $casts = ['started_at' => 'datetime', 'ended_at' => 'datetime'];
    public function user() { return $this->belongsTo(User::class); }
    public function museum() { return $this->belongsTo(Museum::class); }
    public function tour() { return $this->belongsTo(Tour::class); }
    public function events() { return $this->hasMany(VisitEvent::class, 'session_id'); }
}
