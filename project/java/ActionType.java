package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class ActionType  {

  private List<FieldType> field;
  private List<FieldRefType> fieldRef;
  private List<ComponentType> component;
  private List<ComponentRefType> componentRef;
  private List<GroupRefType> groupRef;
  private List<MessageRefType> messageRef;
  private List<TriggerType> trigger;
  private List<TimerSchedule> timerSchedule;
  private List<GroupType> group;
  private List<String> assign;


}