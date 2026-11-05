package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One thing an action does: send a message, set a value, fire a transition or schedule a timer. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActionStepV11  {

  private OrchestraMessageRefV11 fixrMessageRef;
  private String fixrAssign;
  private OrchestraTriggerV11 fixrTrigger;
  private OrchestraTimerScheduleV11 fixrTimerSchedule;


}